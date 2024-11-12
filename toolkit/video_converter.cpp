#include <iostream>
#include <string>
#include <libavformat/avformat.h>
#include <libavcodec/avcodec.h>
#include <libavutil/opt.h>

extern "C" {

    bool convert_to_x264(const std::string &input_file, const std::string &output_file) {
        AVFormatContext *input_format_ctx = nullptr;
        AVFormatContext *output_format_ctx = nullptr;
        AVCodecContext *input_codec_ctx = nullptr, *output_codec_ctx = nullptr;
        AVCodec *input_codec = nullptr, *output_codec = nullptr;
        AVPacket packet;
        int video_stream_index;

        // Открытие входного файла
        if (avformat_open_input(&input_format_ctx, input_file.c_str(), nullptr, nullptr) < 0) {
            std::cerr << "Could not open input file" << std::endl;
            return false;
        }

        if (avformat_find_stream_info(input_format_ctx, nullptr) < 0) {
            std::cerr << "Could not find stream information" << std::endl;
            return false;
        }

        // Поиск видео потока
        video_stream_index = -1;
        for (int i = 0; i < input_format_ctx->nb_streams; i++) {
            if (input_format_ctx->streams[i]->codecpar->codec_type == AVMEDIA_TYPE_VIDEO) {
                video_stream_index = i;
                break;
            }
        }

        if (video_stream_index == -1) {
            std::cerr << "Could not find video stream" << std::endl;
            return false;
        }

        // Открытие кодека
        input_codec = avcodec_find_decoder(input_format_ctx->streams[video_stream_index]->codecpar->codec_id);
        input_codec_ctx = avcodec_alloc_context3(input_codec);
        if (avcodec_parameters_to_context(input_codec_ctx, input_format_ctx->streams[video_stream_index]->codecpar) < 0) {
            std::cerr << "Failed to copy codec parameters to context" << std::endl;
            return false;
        }

        if (avcodec_open2(input_codec_ctx, input_codec, nullptr) < 0) {
            std::cerr << "Failed to open codec" << std::endl;
            return false;
        }

        // Создание выходного контекста
        avformat_alloc_output_context2(&output_format_ctx, nullptr, nullptr, output_file.c_str());
        if (!output_format_ctx) {
            std::cerr << "Could not create output context" << std::endl;
            return false;
        }

        output_codec = avcodec_find_encoder(AV_CODEC_ID_H264);
        if (!output_codec) {
            std::cerr << "Codec not found" << std::endl;
            return false;
        }

        output_codec_ctx = avcodec_alloc_context3(output_codec);
        output_codec_ctx->bit_rate = 2000000; // Битрейт
        output_codec_ctx->width = input_codec_ctx->width;
        output_codec_ctx->height = input_codec_ctx->height;

        if (avcodec_open2(output_codec_ctx, output_codec, nullptr) < 0) {
            std::cerr << "Failed to open encoder" << std::endl;
            return false;
        }

        // Здесь нужно добавить код для обработки видео и записи потока в новый файл
        // Например, преобразование кадров и их кодирование в новый формат.

        return true;
    }
}
