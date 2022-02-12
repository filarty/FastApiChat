document.querySelector("#btn_reg").onclick = () => {
    let username = document.getElementById("username").value;
    let pass = document.getElementById("inputPassword").value;
    eel.send_register_form(username, pass)((n) => {
        console.log(n);
      if (n["detail"] == "user has registered!") {
        document.getElementById("wrongLogin").innerHTML = "Логин занят!";
          }
      else if (n["password"] == "not valid" || n["detail"][0]['msg'] == "ensure this value has at least 6 characters"){
          document.getElementById("wrongLogin").innerHTML = "Пароль должен иметь не менее 6 символов, содержать хотя бы один символ, цифру и Заглавную, маленькую букву!";
            };
          });
       };