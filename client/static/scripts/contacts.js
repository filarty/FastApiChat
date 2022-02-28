eel.get_username()((username) => {
document.getElementById("UserName").innerHTML = username;
});


eel.get_contacts()((names) => {
let doc = document.getElementById("Contacts");
names.forEach(element => {
let li = document.createElement("li");
li.innerHTML = element;
doc.appendChild(li);
    });
});