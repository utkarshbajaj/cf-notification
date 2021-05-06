var firebaseConfig = {
	apiKey: "AIzaSyAbDswr80bHOXsVMWazVQ4Hd88lDrVv_ho",
	authDomain: "cfrankingupdate-90b5b.firebaseapp.com",
	databaseURL: "https://cfrankingupdate-90b5b-default-rtdb.firebaseio.com",
	projectId: "cfrankingupdate-90b5b",
	storageBucket: "cfrankingupdate-90b5b.appspot.com",
	messagingSenderId: "971533794427",
	appId: "1:971533794427:web:a518e3e1d50bc58dd0f6de"
};
// Initialize Firebase

firebase.initializeApp(firebaseConfig);
var firestore = firebase.firestore();

const useremail = document.getElementById('emailbox');
const userhandle = document.getElementById('handlebox');
const username = document.getElementById('namebox');

const saveButton = document.querySelector("#insertbutton");

saveButton.addEventListener("click", function() {
	const handleToSave = userhandle.value;
	const nameToSave = username.value;
	const emailToSave = useremail.value;

	const docRef = firestore.doc("users/" + handleToSave);

	console.log("Handle that user has inserted is " + handleToSave);

	docRef.set({
		userhandle: handleToSave,
		username: nameToSave,
		useremail: emailToSave
	}).then(function() {
		console.log("Status saved!");
	}).catch(function(error) {
		console.log("Got an error: ", error)
	});
})