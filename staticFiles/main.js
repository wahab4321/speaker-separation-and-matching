const profileBtn = document.getElementById('profileBtn');
const profileCard = document.getElementById('profile-card');
const closeCard = document.getElementById('closeCard');

profileBtn.addEventListener('click', ()=>{
    profileCard.style.display = 'block';
});

closeCard.addEventListener('click', ()=>{
    profileCard.style.display = 'none';
});


const dropzoneFile = document.getElementById('dropzone-file');
const fileChosen = document.getElementById('file-chosen');

dropzoneFile.addEventListener('change', function(){
    fileChosen.textContent = this.files[0].name
})