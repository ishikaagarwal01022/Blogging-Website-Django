function contactvalidation(){
    var name = document.forms['contact-form']['name'];
    var email = document.forms['contact-form']['email'];
    var country = document.forms['contact-form']['country'];
    var description = document.forms['contact-form']['description'];

    if(name.value == ""){
        window.alert("Enter your Name");
        name.focus()
        return false
    }

    if(email.value == ""){
        window.alert("Enter your Email Address");
        email.focus()
        return false
    }

    if(country.value == ""){
        window.alert("Enter your Country");
        country.focus()
        return false
    }

    if(description.value == ""){
        window.alert("Enter Description");
        description.focus()
        return false
    }

    return true
}