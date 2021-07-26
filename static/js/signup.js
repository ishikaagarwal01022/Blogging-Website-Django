function signupvalidation(){
    var username = document.forms["signup-form"] ["username"];
    var fname = document.forms["signup-form"] ["fname"];
    var lname = document.forms["signup-form"] ["lname"];
    var email = document.forms["signup-form"] ["email"];
    var pass1 = document.forms["signup-form"] ["pass1"];
    var pass2 = document.forms["signup-form"] ["pass2"];

    if(username.value == ""){
        window.alert("Enter Username")
        username.focus()
        return false
    }

    if(fname.value == ""){
        window.alert("Enter First Name")
        fname.focus()
        return false
    }
    if(lname.value == ""){
        window.alert("Enter Last Name")
        lname.focus()
        return false
    }
    if(email.value == ""){
        window.alert("Enter Email Address")
        email.focus()
        return false
    }
    
    
    if(pass1.value == ""){
        window.alert("Enter Password")
        pass1.focus()
        return false
    }
    if(pass2.value == ""){
        window.alert("Retype your Password")
        pass2.focus()
        return false
    }
    if(pass1.value != pass2.value){
        window.alert("Passwords must be same")
        pass2.focus()
        return false
    }

    return true
}