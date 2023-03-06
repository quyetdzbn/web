// console.log('hello')

var updateBtns =document.getElementsByClassName('update-cart')

for(i=0 ;i<updateBtns.length ;i++)
{
    // lắng nghe người dùng làm gì rồi làm cái hàm ở đây là click
    updateBtns[i].addEventListener('click',function(){
        var productId= this.dataset.product
        var action = this.dataset.action
        console.log('productId',productId, 'action',action)
        console.log('user:' ,user)

        if( user==="AnonymousUser"){
            console.log('user not login')
        }
        else{
            updateUserOrder(productId,action)
        }
    })
}

//  lay du lieu productid va action tu csdl sang trang update-item
function updateUserOrder(productId,action){
    console.log('user login, success add')
    var url='update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
    return response.json()
    })
    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}