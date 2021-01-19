<template>
  <div id="app">
    <div class="columns">
      <div class="column">
        <div class="container-img">
            <figure>
              <img id="position" src="./assets/logo1.jpg" alt="Placeholder image">
            </figure>
        </div>   
      </div>

      <div class="column">
        
        <div class="container-form"> 
            <h1 class="title-2">Cadastrar aluno</h1>
            <div id="card-form">

              <div>
                <p v-show="error">Erro ao cadastrar!</p>
                <form method="POST">
                  <div class="input-margin">
                      <label class="label-form">Nome:</label><input name="name" v-model="nameField" type="text" placeholder="Nome" class="input is-rounded">
                  </div>
                  <div class="input-margin">
                    <label class="label-form">Email:</label><input v-model="emailField" type="text" placeholder="E-mail" class="input is-rounded">
                  </div>
                  <div class="input-margin">
                      <label class="label-form">Número:</label><input v-model="numberField" type="text" placeholder="Número" class="input is-rounded">
                  </div>
                  <div class="input-margin">
                      <label class="label-form">Matrícula:</label><input v-model="registerField" type="text" placeholder="Matrícula" class="input is-rounded">
                  </div>
                  <div class="input-margin">
                      <label class="label-form">Turma:</label><input v-model="class_nField" type="text" placeholder="Turma" class="input is-rounded">
                  </div>
                  <div class="input-margin">
                      <label class="label-form">Turno:</label><input v-model="school_shiftField" type="text" placeholder="Turno" class="input is-rounded">
                  </div>
                </form>
                <button @click="register" id="btn" class="button is-normal">Cadastrar</button>
              </div>

            </div>
        </div>
      </div>

    </div>

    <div class="container-datas">
      
      <input class="input-search" v-model="searching" type="text" placeholder="Pesquise o aluno pelo nome">
      <div class="flex-container">
        <div v-for="student in search" :key="student.id">
          <div class="container-item">
            <Aluno :student="student"  @update="atualizar($event)" @delete="deletar($event)"/>
          </div>
        </div>
 
      </div>
    </div>

  </div>
</template>

<script>
import Aluno from './components/Aluno'

import axios from 'axios'


export default {
  name: 'App',
  created: function() {
    axios.get('http://localhost:8000/student').then(res => {
      this.studentsData = res.data
      console.log(res.data)
      
    })
  },
  data() {
    return {
      error: false,
      nameField: '',
      emailField: '',
      numberField: '',
      registerField: '',
      class_nField: '',
      school_shiftField: '',
      searching: '',
      studentsData: [],
      student_Data: [],
      obj :{},
      data: {}
    }
  },
  methods: {
    register: async function() {
      if(this.nameField == "" || this.nameField === " " || this.nameField.length < 3) {
          this.error = true
      } else {
        this.error = false
        this.data = {
            id : Date.now(),
            name : this.nameField,
            email : this.emailField,
            number : this.numberField,
            registerr : this.registerField,
            class_n : this.class_nField,
            school_shift : this.school_shiftField
          }
        axios.post('http://localhost:8000/register', this.data).then(res => {
          console.log(res)
          return {
            teste: "teste"
          }
        })
        axios.get('http://localhost:8000/student').then(res => {
          this.studentsData = res.data
          console.log(res.data)
        })
      }
      this.nameField = ''
      this.emailField = ''
      this.numberField = ''
      this.registerField = ''
      this.class_nField = ''
      this.school_shiftField = ''
    },
    deletar: function($event) {
      let id = $event.student_id
      axios.delete(`http://localhost:8000/student/${id}`).then(res => { console.log("deletei ", res)})
      axios.get('http://localhost:8000/student').then(res => {
        this.studentsData = res.data
      })
    },
    atualizar: function($event) {
      let id = $event.student_id
      this.data = {
        id : id,
        name : $event.student.name,
        email : $event.student.email,
        number : $event.student.number,
        registerr : $event.student.register,
        class_n : $event.student.class_n,
        school_shift : $event.student.school_shift
      }
      axios.put(`http://localhost:8000/student/${id}`, this.data).then(res => {
        console.log(res.data)
      })
       axios.get('http://localhost:8000/student').then(res => {
        this.studentsData = res.data
      }) 
    }
  },
  components: {
    //Form,
    Aluno
  },
  computed: {
    search: function() {
      if(this.searching == '' | this.searching == ' ') {
        return this.studentsData
      } else {
        return this.studentsData.filter(student => !student.name.toLowerCase().indexOf(this.searching.toLowerCase()))
      }
    }
  }
}
</script>

<style>

.container-img {
  position: relative;
  top: 50%;
  left: 25%;
}

.container-datas {
  position: relative;
  margin-top: 20%;
}

.container-img-TESTE {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-25%,-0%);
}

.container-form {
  position: relative;
  top: 30%;
  width: 75%;

}

#card-form {
  border: 1px solid #aaa;
  border-radius: 10px;
  min-height: 100px;
  padding: 50px;
}

.container-item {
  margin: 20px !important;
  background-color: #6184FF;
  min-height: 200px;

  padding: 15px;
  border-radius: 10px;

}

.flex-container {
  margin: 10px;
  display: grid ;
  
  grid-template-columns: 25% 25% 25% 25%;
}

/* Form CSS */

.label-form {
  width: 20%;
  margin-right: -20px;
}
input {
  border-color: #111;
  margin-top: -5px;
}
.input-margin {
  margin-bottom: 20px;
  display: flex;

}

.input-search { 
  width: 300px;  
  border: 1px solid #aaa;
  margin-left: 50px;
  padding: 5px 10px;
  border-radius: 5px;
}

#btn {
  width: 140px;
  border-radius: 10px;
  color: white;
  background-color: #6184FF;
  
  position: relative;
  float: right;
}


</style>
