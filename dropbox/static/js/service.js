dropboxPlus.factory('Auth', function($http){
    var user;
    return{
        setUser : function(aUser){
            user = aUser;
        },
        isLoggedIn : function(){
            return(user)? user : false;
        },
        logout : function(){
            user = '';
        }
      }
    });