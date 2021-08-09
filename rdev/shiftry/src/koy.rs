use std::hash::{Hash, Hasher};
use std::mem::discriminant;

#[derive(Clone, Copy, PartialEq)]
pub struct Koy(pub rdev::Key);

impl Eq for Koy {}

#[allow(clippy::derive_hash_xor_eq)]
impl Hash for Koy {
    fn hash<H: Hasher>(&self, state: &mut H) {
        discriminant(&self.0).hash(state);
        if let rdev::Key::Unknown(u) = self.0 {
            u.hash(state);
        }
    }
}
