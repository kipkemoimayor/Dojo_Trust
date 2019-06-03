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
// $(".follow").click(function() {
//   $(".following").show()
//   $(".follow").hide()
//
//
// })
// $(".following").click(function() {
//   $(".follow").show()
//   $(".following").hide()
//
//
// })


})

// $(document).ready(function(){
//   $("#prompt").click(function(){
//     swal({
//       button:false,
//       text:"heu",
//       className:'red-bg',
//       closeOnEsc:true,
//       '<div>
//       <a href="">Login<a>
//       </div>'
//
//
//     })
//
//   })
// })
