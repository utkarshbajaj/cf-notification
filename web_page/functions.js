// Initialize Firebase

firebase.initializeApp(firebaseConfig);
var firestore = firebase.firestore();


function myFunction() {
	var x = document.getElementById("frm1");
	const handleToSave = x.elements[1].value;
	const nameToSave = x.elements[0].value;
	const emailToSave = x.elements[2].value;

	console.log("Handle that user has inserted is " + handleToSave);

	if((nameToSave=="") || (emailToSave=="") || (handleToSave=="")){
		alert("Please fill all fields!");
		return;
	}

	const docRef = firestore.doc("users/" + handleToSave);

	docRef.set({
		userhandle: handleToSave,
		username: nameToSave,
		useremail: emailToSave
	}).then(function() {
		console.log("Status saved!");
		alert("Saved successfully!");
	}).catch(function(error) {
		console.log("Got an error: ", error)
	});

}
