mod koy;
use koy::Koy;
use rdev::{EventType, listen, simulate};
use std::thread;
use std::sync::mpsc;
use std::time::{Duration, Instant};
use std::collections::HashSet;

#[derive(PartialEq)]
enum State {
    Quit,
    Wait,
    Hold,
    Spam,
}

fn signal_from_listen(sender: mpsc::Sender<State>) -> Result<(), rdev::ListenError> {
    let mut held_koys = HashSet::<Koy>::new();
    listen(move |event| {
        let pressed_koy = match event.event_type {
            EventType::KeyPress(key) => {
                let koy = Koy(key);
                held_koys.insert(koy);
                Some(koy)
            },
            EventType::KeyRelease(key) => {
                held_koys.remove(&Koy(key));
                None
            },
            _ => None,
        };
        if let Some(pressed_koy) = pressed_koy {
            let binding_triggered = |bound_keys: &[rdev::Key]| {
                let pressed_in_bound = bound_keys.iter().any(|k| Koy(*k) == pressed_koy);
                let bound_are_held = bound_keys.iter().all(|k| held_koys.contains(&Koy(*k)));
                pressed_in_bound && bound_are_held
            };
            use rdev::Key as K;
            if /****/ binding_triggered(&[K::ControlLeft, K::Escape]) {
                sender.send(State::Quit).unwrap();
            } else if binding_triggered(&[K::ControlLeft, K::Tab]) {
                sender.send(State::Hold).unwrap();
            } else if binding_triggered(&[K::ControlLeft, K::BackQuote]) {
                sender.send(State::Spam).unwrap();
            }
        }
    })?;
    Ok(())
}

fn transition_from_signals(initial: State, signals: &mpsc::Receiver<State>) -> State {
    let mut state = initial;
    loop {
        match signals.try_recv() {
            Err(mpsc::TryRecvError::Disconnected) => {
                return State::Quit;
            },
            Err(mpsc::TryRecvError::Empty) => {
                return state;
            },
            Ok(signal) => {
                state = if signal == state { State::Wait } else { signal };
            },
        }
    }
}

fn main() {
    let (sender, receiver) = mpsc::channel();
    thread::spawn(|| {
        signal_from_listen(sender).unwrap();
    });
    let period = Duration::from_millis(20);
    let haperiod = period / 2;
    let mut state = State::Wait;
    loop {
        // transition state if signalled
        state = transition_from_signals(state, &receiver);
        // do state
        let start = Instant::now();
        use rdev::Key as K;
        match state {
            State::Quit => {
                println!("quitting!");
                break;
            },
            State::Wait => {
                println!("...");
                thread::sleep((start + period).saturating_duration_since(Instant::now()));
            },
            State::Hold => {
                println!("holding...");
                simulate(&EventType::KeyPress(K::ShiftLeft)).unwrap();
                thread::sleep((start + period).saturating_duration_since(Instant::now()));
            },
            State::Spam => {
                println!("spamming...");
                simulate(&EventType::KeyPress(K::ShiftLeft)).unwrap();
                thread::sleep((start + haperiod).saturating_duration_since(Instant::now()));
                let middle = Instant::now();
                simulate(&EventType::KeyRelease(K::ShiftLeft)).unwrap();
                thread::sleep((middle + haperiod).saturating_duration_since(Instant::now()));
            },
        }
    }
}
