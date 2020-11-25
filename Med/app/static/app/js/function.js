function add_form(dv1, status) {
    dv1 = document.getElementById(dv1);
    status = document.getElementById(status);
    if (status.checked) dv1.style.display = "block";
    else dv1.style.display = "none";
}

// function all_check() {
//     if (!document.form_name.cheks) return;
//     if (!document.form_name.cheks.length)
//         document.form_name.cheks.checked = document.form_name.cheks.checked ? false : true;
//     else
//         for (var i = 0; i < document.form_name.cheks.length; i++)
//             document.form_name.cheks[i].checked = document.form_name.cheks[i].checked ? false : true;
//     check_main = document.getElementById(check_main);
//     check_main.checked = true;
// }


function add_value() {

}