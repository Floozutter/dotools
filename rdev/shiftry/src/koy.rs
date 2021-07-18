use std::hash::{Hash, Hasher};

#[derive(Clone, Copy, PartialEq)]
pub struct Koy(pub rdev::Key);

impl Eq for Koy {}

impl Hash for Koy {
    fn hash<H: Hasher>(&self, state: &mut H) {
        0.hash(state);
    }
}
