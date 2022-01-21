import java.io.File;
import java.io.IOException;

public class ClassSample01 {
    public static void main(String[] args) {
        final String path = "C:\\test\\test.txt";
        File file = new File(path);
        try {
            System.out.println(file.exists()); // Fileの有無を調べる
            System.out.println(file.createNewFile()); // ファイルの生成
        } catch (IOException e) {
            System.out.println("処理に失敗しました。");
            e.printStackTrace();
        }
    }
}