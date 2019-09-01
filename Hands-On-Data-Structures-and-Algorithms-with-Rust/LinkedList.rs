use std::cell::RefCell;
use std::rc::Rc;

type SingleLink = Option<Rc<RefCell<Node>>>;

#[derive(Clone)]
struct Node {
    value: String,
    next: SingleLink,
}

impl Node {
    // A nice and short way of creating a new node
    fn new(value: String) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node {
            value: value,
            next: None,
        }))
    }
}

struct LinkedList {
    head: SingleLink,
    tail: SingleLink,
    pub length: u64
}

impl LinkedList {
    pub fn new_empty() -> LinkedList {
        LinkedList { head: None, tail: None, length: 0 }
    }
}

fn main() {

}
