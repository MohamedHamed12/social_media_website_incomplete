const password = document.querySelector(".password");
const confirmPassword = document.querySelector(".confirmPassword");
const error = document.querySelector(".error");
const submit = document.querySelector(".registerButton");

console.log(password.value);
console.log(confirmPassword.value);
function validation() {
  if (password.value === confirmPassword.value) {
    alert("register success!");
    window.location.href = "/social_app/users/templates/login.html";
  } else {
    error.textContent = "password should be same";
  }
}
submit.addEventListener("click", (e) => {
  e.preventDefault();
  validation();
  console.log(e);
});
