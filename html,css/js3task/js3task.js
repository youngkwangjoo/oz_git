// 제출 이벤트를 받는다 (이벤트 핸들링)

// 제출된 입력 값들을 참조한다

// 입력값에 문제가 있는경우 이를 감지한다. 
// 아이디 6자, 비밀번호 확인체크
//가입환경 인사를 제공한다. 

const form = document.getElementById("form")

form.addEventListener("submit", function(event){
    event.preventDefault()

    let userid = event.target.id.value // 아이디 입력값을 읽는것
    let userpw1 = event.target.pw1.value 
    let userpw2 = event.target.pw2.value 
    let username = event.target.name.value 
    let userphonenumber = event.target.phonenumber.value
    let userposition = event.target.position.value  
    let usergender = event.target.gender.value 
    let useremail = event.target.email.value 
    let userintro= event.target.intro.value 

    if(userid.length < 6){
        alert("아이디가 너무 짧습니다. 6자이상 입력해주세요")
        return
    }

        if(userpw1.length < 8){
        alert("비밀번호가 너무 짧습니다. 8자이상 입력해주세요")
        return
    }


    if(userpw1 !== userpw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }
    document.body.innerHTML = ""
    document.write(
        `<p> ${username}님 회원가입을 축하합니다.<br>
        회원가입시 입력하신 내역은 다음과 같습니다. <br>
        아이디 : ${userid}<br>
        이름 : ${username}<br>
        전화번호 : ${userphonenumber}<br>
        직업 : ${userposition}`
        )

})