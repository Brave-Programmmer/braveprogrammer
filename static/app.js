var burger = document.querySelector('.burger');
var navnext = document.querySelector('.navnext');

burger.addEventListener('click',()=>{
    navnext.classList.toggle('none');
})