function proceed(){
		 var x = document.getElementById("pref1");
		 var y = document.getElementById("pref2");
		 var z = document.getElementById("pref3");
		 var a = document.getElementById("pref4");
		 var b = document.getElementById("pref5");
			if (x.style.display === "none" && document.getElementById("programming").checked) {
        		x.style.display = "block";
    		};
    		if (document.getElementById("programming").checked === false) {
        		x.style.display = "none";
    		};
    		if (y.style.display === "none" && document.getElementById("net").checked) {
        		y.style.display = "block";
        	};
        	if (document.getElementById("net").checked === false) {
        		y.style.display = "none";
    		};
    		if (z.style.display === "none" && document.getElementById("hardware").checked) {
        		z.style.display = "block";
        	};
        	if (document.getElementById("hardware").checked === false) {
        		z.style.display = "none";
    		};
    		if (a.style.display === "none" && document.getElementById("mobile").checked) {
        		a.style.display = "block";
        	};
        	if (document.getElementById("mobile").checked === false) {
        		a.style.display = "none";
    		};
    		if (b.style.display === "none" && document.getElementById("os").checked) {
        		b.style.display = "block";
        	};
        	if (document.getElementById("os").checked === false) {
        		b.style.display = "none";
    		};
            document.getElementById("submit_div").style.display = "block";
		}

function text_area(){
            if (document.getElementById("other").checked === true) {
                document.getElementById("textarea").disabled = false;
            }else{
                document.getElementById("textarea").disabled = true;
            };
            if (document.getElementById("otherP").checked === true) {
                document.getElementById("inP").disabled = false;
            }else{
                document.getElementById("inP").disabled = true;
            };
            if (document.getElementById("otherS").checked === true) {
                document.getElementById("inS").disabled = false;
            }else{
                document.getElementById("inS").disabled = true;
            };
            if (document.getElementById("otherSO").checked === true) {
                document.getElementById("inSO").disabled = false;
            }else{
                document.getElementById("inSO").disabled = true;
            };
            if (document.getElementById("otherH").checked === true) {
                document.getElementById("inH").disabled = false;
            }else{
                document.getElementById("inH").disabled = true;
            };
            if (document.getElementById("otherPM").checked === true) {
                document.getElementById("inPM").disabled = false;
            }else{
                document.getElementById("inPM").disabled = true;
            };
        }