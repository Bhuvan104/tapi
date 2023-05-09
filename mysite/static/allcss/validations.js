const form=document.getElementById("form")
const username=document.getElementById("id_first_name")
const email=document.getElementById("id_email_address")
const password=document.getElementById("id_password")
const cpassword=document.getElementById("id_cpassword")
const box=document.getElementById("id_checkbox")

form.addEventListener('submit',(e) =>{
    validate()
})

function validate(){
    let namevalue=username.value.trim();
    let useremail=email.value.trim();
    let userpassword=password.value.trim();
    let usercpassword=cpassword.value.trim();
    if (namevalue ===''){
        setError(username,'Username cannot be empty')
    }
    else if (namevalue.length<3){
        setError(username,'Username should be min 3 charaters')
    }
    else {
        setSuccess(username)
    }

    if (useremail ===''){
        setError(email,'Username cannot be empty')
    }
    else if (useremail.length<3){
        setError(email,'Username should be min 3 charaters')
    }
    else {
        setSuccess(email)
    }


    if (userpassword ===''){
        setError(password,'Username cannot be empty')
    }
    else if (userpassword.length<8){
        setError(password,'Username should be min 8 charaters')
    }
    else {
        setSuccess(password)
    }


    if (usercpassword ===''){
        setError(cpassword,'Username cannot be empty')
    }
    else if (usercpassword !== userpassword){
        setError(cpassword,'password and confirm password should be same')
    }
    else {
        setSuccess(cpassword)
    }
    if(!box.checked){
        setError(box,'Please check terms and conditions')
    }
    

}

function setError(input,message){
    let parent=input.parentElement;
    let small=parent.querySelector('small');
    small.innerText=message;
    parent.classList.add('error')
    parent.classList.remove('success')

}

function setSuccess(input){
    let parent=input.parentElement;
    parent.classList.add('success');
    parent.classList.remove('error');
}