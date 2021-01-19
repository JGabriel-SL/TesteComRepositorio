<template>
    <div >
        <div class="datas">
            <p>
                <label class="principal-content">Aluno:</label>
                <label v-show="notModifyName"> {{student.name}}</label> 
                <input class="input-modify" type="text"  v-show="modifyName" v-model="nameField">
            </p>
            
            <p>
                <label class="principal-content">E-mail:</label>
                <label v-show="notModifyEmail"> {{student.email}}</label>
                <input class="input-modify" type="text"  v-show="modifyEmail" v-model="emailField">

            </p>
            <p>
                <label class="principal-content">Número:</label> 
                <label v-show="notModifyNumber"> {{student.number}}</label>
                <input class="input-modify" type="text"  v-show="modifyNumber" v-model="numberField">

            </p>
            <p>
                <label class="principal-content">Matrícula:</label> 
                <label v-show="notModifyRegister"> {{student.register}}</label>
                <input class="input-modify" type="text"  v-show="modifyRegister" v-model="registerField">

            </p>
            <p>
                <label class="principal-content">Turma:</label> 
                <label v-show="notModifyClass"> {{student.class_n}}</label>
                <input class="input-modify" type="text"  v-show="modifyClass" v-model="class_nField">

            </p>
            <p>
                <label class="principal-content">Turno:</label> 
                <label v-show="notModifyShift"> {{student.school_shift}}</label>
                <input class="input-modify" type="text"  v-show="modifyShift" v-model="school_shiftField">

            </p>
            
        </div>
        <div>
            <button class="button button-delete is-danger is-light" @click="emitirDelete">delete</button>
            <button v-show="buttonShow_Update" class="button is-info is-light" @click="update">atualizar</button>
            <button  v-show="buttonShow_conclude" class="button button-atualizar is-success" @click="conclude">Concluir</button>

        </div>
    </div>
</template>

<script>

export default {
    created: function() {
        this.nameField = this.student.name
        this.emailField = this.student.email,
        this.numberField = this.student.number,
        this.registerField = this.student.register,
        this.class_nField = this.student.class_n,
        this.school_shiftField = this.student.school_shift
        this.student_id = this.student.id

    },
    data() {
        return {
            notModifyName : true,
            notModifyEmail : true,
            notModifyNumber : true,
            notModifyRegister : true,
            notModifyClass : true,
            notModifyShift : true,
            modifyName : false,
            modifyEmail : false,
            modifyNumber : false,
            modifyRegister : false,
            modifyClass : false,
            modifyShift : false,
            
            buttonShow_conclude: false,
            buttonShow_Update: true,

            nameField: '',
            emailField: '',
            numberField: '',
            registerField: '',
            class_nField: '',
            school_shiftField: '',
            student_id: 0,
            update_student: {}
            
        }
    },
    props: {
        student: Object,
    },
    methods: {
        emitirDelete: function() {
            this.$emit('delete', {student: this.student, student_id: this.student.id})
            console.log('emitir delete')
        },
        update: function() {
            if(this.buttonShow_Update){
                this.buttonShow_Update = false
                this.buttonShow_conclude = true

                this.modifyName = true
                this.modifyEmail = true
                this.modifyNumber = true
                this.modifyRegister = true
                this.modifyClass = true
                this.modifyShift = true

                this.notModifyName = false
                this.notModifyEmail = false
                this.notModifyNumber = false
                this.notModifyRegister = false
                this.notModifyClass = false
                this.notModifyShift = false


                // Update Data

                
            }

        },
        conclude: function() {
              if(this.buttonShow_conclude){
                this.buttonShow_Update = true
                this.buttonShow_conclude = false

                this.modifyName = false
                this.modifyEmail = false
                this.modifyNumber = false
                this.modifyRegister = false
                this.modifyClass = false
                this.modifyShift = false

                this.notModifyName = true
                this.notModifyEmail = true
                this.notModifyNumber = true
                this.notModifyRegister = true
                this.notModifyClass = true
                this.notModifyShift = true

                this.update_student = {
                id : this.student.id,
                name : this.nameField,
                email : this.emailField,
                number : this.numberField,
                register : this.registerField,
                class_n : this.class_nField,
                school_shift : this.school_shiftField
            }
                this.$emit('update', {student: this.update_student, student_id: this.student.id})
                console.log('emitir update')

            }

        }
    }
}
</script>

<style scoped>
    p {
        font-weight: 600;
        color: black
    }

    .principal-content {
        color: white;
    }

    .datas {
        margin-bottom: 10px;
    }

    .button-delete {
        float: right;
    }    

    .input-modify {
        margin-left: 5px;
        border: 1px solid #aaa;
        border-radius: 5px;
    }

 
</style>