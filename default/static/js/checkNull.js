        function checkNull(id){
            x = document.getElementById(id);
            if(!x.getAttribute('value')){
                var y = x.nextSibling;
                y.innerHTML = '此项不能为空！';
            }
            else
            {
                var y = x.nextSibling;
                y.innerHTML = null;
            }
        }

        function listenInput(event,id){
            x = document.getElementById(id);
            var getIn = event.target;
            x.setAttribute('value',getIn.value);
        }