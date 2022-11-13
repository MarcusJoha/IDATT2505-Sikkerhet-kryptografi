

fn replace(msg: &str) -> String {
    return msg
    .replace("&", "&amp")
    .replace("<", "&lt")
    .replace(">","&gt");
}

fn main() {

    let msg: &str = "< < & & > >";
    println!("Orginal string: {}", msg);
    println!("Med replace: {}", replace(msg));
}