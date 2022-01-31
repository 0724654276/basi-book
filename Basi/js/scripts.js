let route_price;
let total = 0;

function mybooking(route, category,total) {
    this.route = route;
    this.category = category;
    this.total = total;
    
}


$().ready(function(){
    $(function () {
         $('#summary').hide();
 
//Get the user input values in each section;
        $('#btn-submit').click(function(event) {
            event.preventDefault();
            let route = $("#route option:selected").val();
            let category = $("#category option:selected").val();
            let number = $('#seat_no').val();
            alert(route);

            switch (route) {
                case route= "mombasa":
                    if (category === "first") {
                        route_price = 1500;  
                    } else if (category=== "second") {
                        route_price = 1000;
                    } else if (category === "economy") {
                        route_price = 700;
                    }
                    else {
                        route_price = 1150;
                

                    }
                    
                    break;


                case route= "nairobi":
                    if (category === "first") {
                        route_price = 1600;  
                    } else if (category === "second") {
                        route_price = 1050;
                    } else if (cateory=== "economy") {
                        route_price = 750;
                    }
                    else {
                        route_price = 1200;
                    }
                    
                    break;

                case route = "kisumu":
                        if (category === "first") {
                            route_price = 1550;  
                        } else if (category === "second") {
                            route_price = 950;
                        } else if (category === "economy") {
                            route_price = 750;
                        }
                        else {
                            route_price = 1000;
                        }
                        
                        break; 
                     
                    


                        

            
            }

            
            total = route_price ;
            let total2 = total * number;
            let checkoutTotal = total2;


         $("#routename").html( $("#routes option:selected").val());
         $("#categoryname").html(category);
         
         $("#number").html( $('#seat_no').val());
        
         $("#urtotals").html(checkoutTotal);


        });
        $("button#btn-submit").click(function(){ 

        
            $('#summary').show();


            
          });

    });
    

});
