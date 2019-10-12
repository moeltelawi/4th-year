/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package caesarcipher;

/**
 *
 * @author Mo Eltelawi
 */
public class CaesarCipher {

    public static String encrypt(String text, int s) {
        String result = "";

        for (int i = 0; i < text.length(); ++i) {
            char ch = text.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                ch = (char) (ch + s);

                if (ch > 'z') {
                    ch = (char) (ch - 26);
                }

                result += ch;
            } else if (ch >= 'A' && ch <= 'Z') {
                ch = (char) (ch + s);

                if (ch > 'Z') {
                    ch = (char) (ch - 26);
                }

                result += ch;
            } else {
                result += ch;
            }
        }
        return result;

    }

    public static String decrypt(String text, int s) {
        String result = "";

        for (int i = 0; i < text.length(); ++i) {
            char ch = text.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                ch = (char) (ch - s);

                if (ch < 'a') {
                    ch = (char) (ch + 26);
                }

                result += ch;
            } else if (ch >= 'A' && ch <= 'Z') {
                ch = (char) (ch - s);

                if (ch < 'A') {
                    ch = (char) (ch + 26);
                }

                result += ch;
            } else {
                result += ch;
            }
        }
        return result;

    }

    public static void main(String[] args) {
        String text = "qwert13436565887990yuiop[]';lkjhgfdsazxcvbnm,./  ";
        int s = 4;
        System.out.println("Text  : " + text);
        System.out.println("Shift : " + s);
        System.out.println("Cipher: " + encrypt(text, s));
        System.out.println("Cipher: " + decrypt(text, s));
    }
}
