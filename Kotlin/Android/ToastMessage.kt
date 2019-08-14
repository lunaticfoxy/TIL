package com.js.kotlin_example

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Find the EditText
        var editText = findViewById<EditText>(R.id.editText);
        editText.setHint("Your name?");

        //Find the Button
        var sendButton = findViewById<Button>(R.id.button);

        //Set on click
        sendButton.setOnClickListener {

            //입력값을 토스트로 뛰운다.
            Toast.makeText(this, "${editText.text}님 반갑습니다.", Toast.LENGTH_LONG).show();

            //에디터텍스트값을 비운다.
            editText.setText("");
        }

    }
}
