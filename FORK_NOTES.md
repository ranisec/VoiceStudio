# ranisec 포크 노트

업스트림: https://github.com/debpalash/VoiceStudio (AGPL-3.0, 라이선스 변경 없음)

## [ranisec fork] - 2026-10-29
### 추가
- `stt.py`: faster-whisper(VoiceStudio 내부 ASR 엔진)로 오디오/영상 파일을 CPU(int8)에서 한국어 전사하는 최소 스크립트.
  - 사용법: `python stt.py <오디오파일> [모델크기=small]` → `[시작-끝] 텍스트` 줄 단위 출력.
  - 필요 패키지: `pip install faster-whisper`
  - 외부 전송: 기본값 `HF_HUB_OFFLINE=1`(캐시된 모델만 사용, huggingface.co 접속 안 함), `HF_HUB_DISABLE_TELEMETRY=1`.
    처음 모델을 받을 때만 `HF_HUB_OFFLINE=0`으로 실행. 텔레메트리·업로드 없음.
  - 라이선스: 이 파일은 업스트림과 같은 AGPL-3.0으로 배포합니다. faster-whisper는 MIT.
### 커밋하지 않은 것
- 로컬에서 정리(삭제)한 `electron/build/`, `omnivoice-gallery` 등의 삭제 내역, 로컬 `.venv-stt/`.
