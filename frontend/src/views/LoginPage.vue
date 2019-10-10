<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center text-center justify-center fill-height>
        <v-flex xs3>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Login</span>
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
                    v-model="credentials.username"
                    label="E-mail"
                    color="black"
                    required
                  />
                  <v-text-field
                    type="password"
                    v-model="credentials.password"
                    color="black"
                    label="Password"
                    maxlength="20"
                    required
                    @keyup.enter="login"
                  />
                </v-container>
                <v-btn color="red darken-4" class="white--text"  :disabled="!valid" @click="login">Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    name: 'Login',
    data: () => ({
        credentials: {},
        valid:true,
        loading:false
    }),
    methods: {
        login() {
          // checking if the input is valid
            if (this.$refs.form.validate()) {
              this.loading = true;
              axios.post('http://localhost:8000/api/login/', this.credentials).then(res => {
                this.$store.state.login = true;
                this.$session.start();
                this.$session.set('token', res.data.token);
                this.$session.set('id', this.credentials.username);
                alert("로그인 성공");
                router.push('/');
                
                // eslint-disable-next-line
              }).catch(e => {
                this.loading = false;
              });
            }
        }
    }
}
</script>
<style>



</style>
