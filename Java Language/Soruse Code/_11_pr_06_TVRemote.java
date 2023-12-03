interface TVRemote{
    void Channel();
    void Volume();
}
interface SmartTVRemote{
    void Youtube();
    void Voice_Control();
}

class TV implements TVRemote,SmartTVRemote{
    @Override
    public void Channel() {
        System.out.printf("Channel 45\n");
    }
    @Override
    public void Volume() {
        System.out.printf("Volume is 25%\n");
    }
    @Override
    public void Voice_Control() {
        System.out.printf("Hey!! Googgle");
    }
    @Override
    public void Youtube() {
        System.out.printf("Watching Youtube Shorts");
    }
}

public class _11_pr_06_TVRemote {
    public static void main(String[] args) {
        TV object = new TV();
        object.Youtube();
    }
}
