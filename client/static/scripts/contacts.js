const USER = document.cookie.split(";")[1].split("=")[1];


document.getElementById("username").innerHTML = USER;


eel.get_contacts()((names) => {
    let doc = document.querySelector(".users");
    names.forEach(element => {
    let li = document.createElement("li");
    li.innerHTML =  `<li class='person' data-chat='person1'><div class='user'><img src='https://www.bootdey.com/img/Content/avatar/avatar3.png' alt='Retail Admin'><span class='status busy'></span></div><p class='name-time'><span class='name'>${element}</span><span class='time'>15/02/2019</span></p></li>`;
    doc.appendChild(li);
        });
    });