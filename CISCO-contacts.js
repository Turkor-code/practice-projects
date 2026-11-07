let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
}];

let done = false;
while (done != true) {
    let endCont = contacts.length - 1;
    let choice = prompt("First Cont (1) | Last Cont (2) | All Conts (3) | Add new (4) | EXIT (5)");
    
    // processes
    if (choice == "1") {
        console.log(contacts[0].name + "||||" + contacts[0].phone + "||||" + contacts[0].email);
    } else if (choice == "2") {
        console.log(contacts[endCont].name + "||||" + contacts[endCont].phone + "||||" + contacts[endCont].email);
    } else if (choice == "3") {
        for (let keys in contacts) {
            console.log(`${contacts[keys].name} |||| ${contacts[keys].phone} |||| ${contacts[keys].email}`);
        }
    } else if (choice == "4") {
        let name1 = prompt("Enter name");
        let phone1 = prompt("Enter phone");
        let email1 = prompt("Enter email");
        newCont = {
            name: name1,
            phone: phone1,
            email: email1
        };
        contacts.push(newCont)
    } else if (choice == "5") {
        done = true;
        break;
    } 
}