package crypto;

/**
 *
 * @author Mo Eltelawi
 */
public class Feistel {

    static public String encrypt(String text, String key, String fun) {

        int n = text.length();
        String lPart = text.substring(0, n / 2);
        String rPart = text.substring(n / 2);
        int x = Integer.parseInt(lPart, 2);
        int y = Integer.parseInt(rPart, 2);
        int k = Integer.parseInt(key, 2);

        int tleft, tright;

        for (int i = 0; i < 16; i++) {
            tleft = tright = y;
            

            if (fun == "AND") {
                tright = y & k;
            }
            if (fun == "OR") {
                tright = y | k;
            }
            if (fun == "XOR") {
                tright = y ^ k;
            }

            y = tright ^ x;
            x = tleft;

        }
        int temp = y;
        y = x;
        x = temp;

        lPart = Integer.toBinaryString(x);
        rPart = Integer.toBinaryString(y);

        if (lPart.length() < n / 2) {
            for (int i = 0; i <= ((n / 2) - lPart.length()); i++) {
                lPart = '0' + lPart;
            }
        }

        if (rPart.length() < n / 2) {
            for (int i = 0; i <= ((n / 2) - rPart.length()); i++) {
                rPart = '0' + rPart;
            }
        }
        String cipher = new String("");
        cipher = lPart + rPart;
        return cipher;
    }

    static public String decrypt(String text, String key, String fun) {
        String plainText = new String("");
        int n = text.length();
        String lPart = text.substring(0, n / 2);
        String rPart = text.substring(n / 2);
        int x = Integer.parseInt(lPart, 2);
        int y = Integer.parseInt(rPart, 2);
        int k = Integer.parseInt(key, 2);

        int tleft, tright;

        for (int i = 0; i < 16; i++) {
            tleft = tright = y;
            

            if (fun == "AND") {
                tright = y & k;
            }
            if (fun == "OR") {
                tright = y | k;
            }
            if (fun == "XOR") {
                tright = y ^ k;
            }

            y = tright ^ x;
            x = tleft;

        }
        int temp = y;
        y = x;
        x = temp;

        lPart = Integer.toBinaryString(x);
        rPart = Integer.toBinaryString(y);

        if (lPart.length() < n / 2) {
            for (int i = 0; i <= ((n / 2) - lPart.length()); i++) {
                lPart = '0' + lPart;
            }
        }

        if (rPart.length() < n / 2) {
            for (int i = 0; i <= ((n / 2) - rPart.length()); i++) {
                rPart = '0' + rPart;
            }
        }

        plainText = lPart + rPart;
        return plainText;
    }

}
