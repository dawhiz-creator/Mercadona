let email = 'dawhiz@live.fr';
let link = document.getElementById('email-link');
link.setAttribute('href', 'mailto:' + email.replace(/@/g, '&#64;'));

link.addEventListener('click', function(event) {
  event.preventDefault();
  window.location.href = 'mailto:' + email;
});


