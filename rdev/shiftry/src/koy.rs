use std::hash::{Hash, Hasher};
use std::mem::discriminant;

#[derive(Clone, Copy, PartialEq)]
pub struct Koy(pub rdev::Key);

impl Eq for Koy {}

impl Hash for Koy {
    fn hash<H: Hasher>(&self, state: &mut H) {
        discriminant(&self.0).hash(state);
        match self.0 {
            rdev::Key::Unknown(u) => {
                u.hash(state);
            },
            _ => {},
        }
    }
}
