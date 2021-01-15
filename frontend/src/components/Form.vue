<template>
  
</template>

<script>
export default {
    data() {
        return {
            error: false,
            errorName: false ,
            nameField: '',
            emailField: '',
            numberField: '',
            registerField: '',
            class_nField: '',
            school_shiftField: ''
        }
    },
    props: {
        student: Object
    },
    methods: {
        register: function() {
            if(this.nameField == "" || this.nameField === " " || this.nameField.length < 3) {
                this.error = true
            } else {
                this.student.push({
                    name: this.nameField,
                    email: this.nameField,
                    number: this.nameField,
                    register: this.nameField,
                    class_n: this.class_nField,
                    school_shift: this.school_shiftField
                })
            }
        },
        emitir: function() {
            this.$emit('teste', {teste: 'teste'})
            console.log('testando')
        }
    }
}
</script>

<style scoped>

    label {
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

    #btn {
        width: 140px;
        border-radius: 10px;
        color: white;
        background-color: #6184FF;
        
        position: relative;
        float: right;
    }

    

</style>