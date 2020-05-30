{% extends 'layouts/default/page.html' %}
{% load static %}
{% load bootstrap4 %}
{% load i18n %}
{% block content %}
{% csrf_token %}

<style>
  /* .navbar{
    display: none;
  } */
  
  /* width */
  ::-webkit-scrollbar {
    width: 10px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #f1f1f1; 
  }
  
  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888; 
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #555; 
  }
</style>
<!-- <div class="btn_reload sticky"><button class="reload" onclick="reload()"><i class="fas fa-redo"></i></button></div><br> -->
{% if request.user.is_authenticated %}

                  <div class="grid_main">
                    <button id="user_btn" onclick="show_user()" style="display: block;float: right;">{{ request.user.first_name }}</button>
                    <button class="btn" style="display: block;float: left;">Compose</button>
                  </div>
                  <br>
                  <br>
                    <div id="btnContainer">
                      <!-- <button class="btn" id="show" onclick="listView()"><i class="fa fa-bars"></i></button> 
                      <button class="btn active" id="hide" onclick="gridView()"><i class="fa fa-th-large"></i></button> -->
                    </div>
                    <br>
                    <div id="list_con">
                      {%for file in all_files%}
                      <div class="row">
                        <div class="column">
                          <h6>{{file.file_field}}</h6>
                          
                        </div>
                      </div>
                      {% endfor %}
                    </div>
                    <div class="boxes">
                      <div id="u_details" class="user">
                        
                      </div>
                      <div id="grid_con" >
                        <div class="grid-container" >
                          <script type="text/javascript" >
                            var thumbnail_img = [];
                            var fi