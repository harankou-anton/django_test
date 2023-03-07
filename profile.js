
document.addEventListener("DOMContentLoaded", function() {
  function showMessage() {
    let message = "Data was saved";
    alert(message);
  }

  const button = document.getElementById("send-button");

  button.addEventListener("click", showMessage);
});
