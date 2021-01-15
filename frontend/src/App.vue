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
                <form>
                  <div class="input-margin">
                      <label class="label-form">Nome:</label><input v-model="nameField" type="text" placeholder="Nome" class="input is-rounded">
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

// import Form from './components/Form'
import Aluno from './components/Aluno'


export default {
  name: 'App',
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
      students: [
        {
          id: 1,
          name: 'João Gabriel',
          email: 'gabriel@gmail.com',
          number: 'xxxx-xxxx',
          register: '123123',
          class_n: '3',
          school_shift: 'Integral'
        },
        {
          id: 2,
          name: 'Giulia Trevisan',
          email: 'giutrevisan@gmail.com',
          number: 'xxxx-xxxx',
          register: '213123',
          class_n: '3',
          school_shift: 'Integral'
        },
        {
          id: 3,
          name: 'João P. Guarany',
          email: 'jp.guarany@gmail.com',
          number: 'xxxx-xxxx',
          register: '414132',
          class_n: '3',
          school_shift: 'Integral'
        },
        {
          id: 4,
          name: 'Everton Wendell',
          email: 'everton_wendell@gmail.com',
          number: 'xxxx-xxxx',
          register: '212321',
          class_n: '3',
          school_shift: 'Integral'
        },
        {
          id: 5,
          name: 'Guilherme Feijo',
          email: 'guilherme@gmail.com',
          number: 'xxxx-xxxx',
          register: '123213',
          class_n: '3',
          school_shift: 'Integral'
        },
        {
          id: 6,
          name: 'Vinicius Mota',
          email: 'Vini.mota@gmail.com',
          number: 'xxxx-xxxx',
          register: '123412',
          class_n: '3',
          school_shift: 'Integral'
        }
      ]
    }
  },
  methods: {
    register: function() {
      if(this.nameField == "" || this.nameField === " " || this.nameField.length < 3) {
          this.error = true
      } else {
        this.error = false
        this.students.push({
            id: Date.now(),
            name: this.nameField,
            email: this.emailField,
            number: this.numberField,
            register: this.registerField,
            class_n: this.class_nField,
            school_shift: this.school_shiftField
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
      console.log("hhahahaha")
      console.log($event)
      let id = $event.student_id
      let newArray = this.students.filter(student => student.id != id)
      this.students = newArray
    },
    atualizar: function($event) {
      let id = $event.student_id
      this.students.forEach(student => {
        if (student.id == id) {
          student.name = $event.student.name
          student.email = $event.student.email
          student.number = $event.student.number
          student.register = $event.student.register
          student.class_n = $event.student.class_n
          student.school_shift = $event.student.school_shift
        }
      });
      
    }
  },
  components: {
    //Form,
    Aluno
  },
  computed: {
    search: function() {
      if(this.searching == '' | this.searching == ' ') {
        return this.students
      } else {
        return this.students.filter(student => !student.name.toLowerCase().indexOf(this.searching.toLowerCase()))
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
