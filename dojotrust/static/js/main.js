$(document).ready(function () {
  $("#prompt").click(function(){
    Swal.fire({
    showConfirmButton:false,
    html:
    '<ul  class="list-group"> <li class="list-group-item"><a class="ref" href="upload">Post</a> </li></ul>'+
    '<ul  class="list-group"> <li class="list-group-item"><a class="ref" href="edit">Edit Profile</a> </li></ul>'+
    '<ul class="list-group"> <li class="list-group-item"><a class="ref" href="/logout">Logout</a> </li></ul>'+
    '<ul class="list-group"> <li class="list-group-item"><a class="ref" href="/accounts/password/change">Change Password</a></li></ul>'+
    '<ul  class="list-group"> <li class="list-group-item"><a class="ref" href="">Cancel</a> </li></ul>',
  })
})

})
