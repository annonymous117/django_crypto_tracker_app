
// $(document).ready(function(){  
//   $(".cbtn").click(function(){
//       $(".moon").toggleClass(" fa-sun");
//       $("body").toggleClass('mydark');
//   });
// });
// $(document).ready(function(){  
//   $("#notify").click(function(){
//       $("#notify").toggleClass("ntfon");
//   });
// });
let mybtn=document.querySelector(".modebtn")
let my_icon=document.querySelector("#icon")
let my_body=document.querySelector("body")
function togglemode(){
   if(my_body.classList.contains("mydark")){
     my_body.classList.remove("mydark")
      localStorage.setItem("theme", "light");
    }else{
    my_icon.classList.add("fa-sun")
    my_body.classList.add("mydark")
    localStorage.setItem("theme", "dark");
   }
}
if (localStorage.getItem("theme") === "dark") {
my_body.classList.add('mydark');
my_icon.classList.add("fa-moon")

}



mybtn.addEventListener('click', togglemode);
$('body').ready(function(){
  var catid;
  catid = $(this).attr("data-catid");
  $.ajax(
  {
      type:"GET",
      url: "/jsonres",
      data:{
               post_id: catid
      },
      success: function( response ) 
      {
        $( 'body') [0] .reset();
      }
   })
});


const searchinp = document.getElementById("srch");
const rows = document.querySelectorAll('tbody tr')

searchinp.addEventListener('keyup' , function(event){
  console.log(event);
  const q =event.target.value.toLowerCase();

  rows.forEach(row =>{
    row.querySelector('td').textContent.toLowerCase().startsWith(q)
     ? null 
     : (row.style.display="none");
  });
});