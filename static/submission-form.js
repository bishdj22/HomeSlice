function SubForm(e){
    e.preventDefault();
    var url=$(this).closest('form').attr('action'),
    data=$(this).closest('form').serialize();
    $.ajax({
        url:url,
        type:'POST',
        data:data,
        success:function(){
            console.log("success")
           //whatever you wanna do after the form is successfully submitted
       }
   });
}
