
document.querySelector("#btn").onclick = () => {
  let username = document.getElementById("username").value;
  let pass = document.getElementById("inputPassword").value;
  eel.send_login_form(username, pass)((n) => {
    if (n["detail"] == "user not registered!") {
      document.getElementById("wrongLogin").innerHTML = "Неверный логин или пароль!";
        };
    if (n["connection"] == "failed") {
        document.getElementById("wrongLogin").innerHTML = "Сервер не доступен!";
          };
        });
     };

document.querySelector("#regButton").onclick = () => {
  window.location.replace("registration.html");
};