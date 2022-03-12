
document.querySelector("#btn").onclick = () => {
  let username = document.getElementById("username").value;
  let pass = document.getElementById("inputPassword").value;
  eel.send_login_form(username, pass)((n) => {
    if (n["response"]["detail"] == "user not registered!") {
      document.getElementById("wrongLogin").innerHTML = "Неверный логин или пароль!";
        };
    if (n["response"] == "failed") {
        document.getElementById("wrongLogin").innerHTML = "Сервер не доступен!";
          };
    if (n["response"]['login'] == "success") {
      document.cookie = `login=${n['login']}`
      window.location.replace("contact_list.html");
    };
        });
     };

    
document.querySelector("#regButton").onclick = () => {
  window.location.replace("registration.html");
};