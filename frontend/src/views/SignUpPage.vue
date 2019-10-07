<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center text-center justify-center fill-height>
        <v-flex xs4>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Sign up</span>
            </v-card-title>
            <v-spacer/>
            <v-card-text>
              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  indeterminate color="black"
                />
              </v-layout>
              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="profile.username"
                    :counter="70"
                    color="black"
                    label="Name"
                    maxlength="70"
                    required
                  />

                  <v-text-field
                    type="password"
                    v-model="profile.password"
                    :counter="20"
                    color="black"
                    label="Password"
                    maxlength="20"
                    required
                  />

                  <v-text-field
                    type="password"
                    v-model="checkPass"              
                    :counter="20"
                    color="black"
                    label="Password Check"
                    maxlength="20"
                    required
                  />

                  <v-text-field
                    type="number"
                    v-model="profile.age"
                    :counter="2"
                    color="black"
                    label="Age"
                    maxlength="20"
                    required
                  />

                  <v-text-field
                    type="string"
                    v-model="profile.occupation"
                    :counter="20"
                    color="black"
                    label="Occupation"
                    maxlength="20"
                    required
                  />

                  <v-radio-group v-model="profile.gender" row >
                    <v-radio color="black" label="Male" value="M"></v-radio>
                    <v-radio color="black" label="Female" value="F"></v-radio>
                  </v-radio-group>

                </v-container>
                <v-btn class="black white--text" :disabled="!valid" @click="sign">Sign</v-btn>

              </v-form>


            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
 /*jslint devel: true */
import axios from 'axios';
import router from '../router';

export default {
    name: 'SignUp',
    data: () => ({
        profile: {},
        checkPass: "",
        valid:true,
        loading:false
    }),
    methods: {
      sign() {
        if(this.profile.password !== this.checkPass){
          alert("Your password is not corrected");
        }else if(this.profile.age.length > 2){
          alert("your age is too much");
        }else{
          if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8000/api/users/', this.profile).then(res => {
              alert("회원가입 되었습니다");
              axios.post('http://localhost:8000/api/login/', {
                username : this.profile.username,
                password : this.profile.password
              }).then(res => {
                this.$store.state.login = true;
                this.$session.start();
                this.$session.set('token', res.data.token);
                this.$session.set('id', this.profile.username);
                alert("회원님께서 보셨던 영화의 평점을 등록해주세요!");
                router.push('/search');
              }).catch( e => {
                console.log(e);
              });
            }).catch( res =>{
              console.log(res);
             });
            this.loading = false;
          }           
        }
      }
    }
}
</script>
