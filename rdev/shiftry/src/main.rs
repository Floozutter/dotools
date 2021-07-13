use rdev::{listen, simulate, EventType, Key};
use std::sync::{Arc, Mutex};
use std::{thread, time};

fn main() {
    let on_a = Arc::new(Mutex::new(false));
    let on_b = on_a.clone();
    let mut backquote_held = false;
    let mut lctrl_held = false;
    let _listener = thread::spawn(move || {
        listen(move |event| {
            let pressed = match event.event_type {
                EventType::KeyPress(k) => {
                    match k {
                        Key::BackQuote => { backquote_held = true; true },
                        Key::ControlLeft => { lctrl_held = true; true },
                        _ => false,
                    }
                },
                EventType::KeyRelease(k) => {
                    match k {
                        Key::BackQuote => { backquote_held = false; },
                        Key::ControlLeft => { lctrl_held = false; },
                        _ => {},
                    };
                    false
                },
                _ => false,
            };
            if pressed && backquote_held && lctrl_held {
                let mut on = on_a.lock().unwrap();
                *on = !*on;
            }
        }).unwrap();
    });
    let period = time::Duration::from_millis(10);
    let pulse = period / 2;
    loop {
        let on = *on_b.lock().unwrap();
        println!("{}", if on { "shiftry!" } else { "..." });
        if on {
            simulate(&EventType::KeyPress(Key::ShiftLeft)).unwrap();
            thread::sleep(pulse);
            simulate(&EventType::KeyRelease(Key::ShiftLeft)).unwrap();
            thread::sleep(pulse);
        } else {
            thread::sleep(period);
        }
    }
}
