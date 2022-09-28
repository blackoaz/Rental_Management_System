//search-btn
//submit-btn

// const searchButton = document.getElementById('search-btn')
// const submitButton = document.getElementById('submit-btn')

// function activate() {
//     if(searchButton.value == ''){
//         submitButton.disabled = True

//     }else(
//         submitButton.disabled = False  
//     )
//     console.log('Hello')
// }
$(document).ready(function(){
    $("button[id='submit-btn']").attr('disabled',true);
    $("input[id='search-btn']").on('keyup',function(){
        if($(this).val != ''){
            $("button[id='submit-btn']").attr('disabled',false);

        }
    });
    
})

const listItems = document.querySelectorAll('.items li')
listItems.forEach(item =>{
    item.addEventListener('click',()=>{
        let isActive = item.classList.contains('active')
        listItems.forEach(el=>{
            el.classList.remove('active')
        })
        if(isActive) item.classList.remove('active');
        else item.classList.add('active');

    });
    
});
console.log(isActive)
