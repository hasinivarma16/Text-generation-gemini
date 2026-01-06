let quote_txt=document.getElementById("quote-txt")
const btn=document.querySelector("#btn");

const quoteFn=async () =>{
quote_txt.textContent="Generating txt plzz.."
try{
	response=await fetch("http://127.0.0.1:8000",{
		method:"POST",
	});
        data=await response.json()
	quote_txt.textContent=data.quote;
}
catch(err){
 console.error(err)
}
};
btn.addEventListener("click",quoteFn);
