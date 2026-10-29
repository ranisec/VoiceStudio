# ranisec 포크 노트 — VoiceStudio

| 항목 | 내용 |
|---|---|
| 업스트림 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) |
| 라이선스 | AGPL-3.0 (업스트림과 동일, 변경 없음) |
| 원본 코드 수정 | 없음 (파일 추가만) |
| 업스트림 PR | 보내지 않음 |

## [ranisec fork] - 2026-10-29

### 추가: `stt.py`
[faster-whisper](https://github.com/SYSTRAN/faster-whisper)(VoiceStudio가 내부적으로 쓰는 ASR 엔진, MIT)로
오디오·영상 파일을 **CPU에서 한국어로 전사**하는 8줄짜리 스크립트입니다. VoiceStudio 앱·서버 없이 단독으로 동작합니다.

**설정값**: 언어 `ko` 고정, `device="cpu"`, `compute_type="int8"`, VAD(무음 구간 건너뛰기) 켬.

#### 설치
```bash
python3 -m venv .venv-stt
.venv-stt/bin/pip install faster-whisper
# 영상·m4a 등은 faster-whisper가 PyAV로 직접 디코딩합니다(별도 ffmpeg 불필요).
```

#### 사용법
```text
python stt.py <오디오/영상 파일> [모델=small]
```
```bash
# 1) 처음 한 번: 모델 다운로드 허용 (huggingface.co 접속)
HF_HUB_OFFLINE=0 .venv-stt/bin/python stt.py sample.wav small

# 2) 이후: 캐시된 모델만 사용 (기본값, 외부 접속 없음)
.venv-stt/bin/python stt.py lecture.mp4
.venv-stt/bin/python stt.py interview.m4a medium > interview.txt
```
출력 형식(한 줄에 한 구간, 초 단위):
```text
[0.0-3.2]  안녕하세요, 오늘은 ...
[3.2-7.9]  첫 번째 주제는 ...
```

| 모델 | 특징 |
|---|---|
| `tiny`, `base` | 가장 빠름, 정확도 낮음 |
| `small` (기본) | 속도·정확도 균형 |
| `medium`, `large-v3` | 더 정확, 훨씬 느리고 메모리 많이 씀 |

#### 개인정보·네트워크
- 기본값 `HF_HUB_OFFLINE=1`: 캐시된 모델만 쓰고 huggingface.co에 접속하지 않습니다.
- `HF_HUB_DISABLE_TELEMETRY=1` 설정. 음성·텍스트를 외부로 보내는 코드는 없습니다.
- 두 값 모두 `setdefault`이므로, 환경 변수로 직접 지정하면 그 값이 우선합니다.

#### 문제 해결
- 모델 파일을 찾을 수 없다는 오류(예: `LocalEntryNotFoundError`) → 아직 모델이 캐시에 없습니다. 위 1)처럼 `HF_HUB_OFFLINE=0`으로 한 번 실행하세요.
- 너무 느림 → 더 작은 모델(`base`)을 쓰거나 파일을 나눠서 처리하세요.

### 포함하지 않은 것
- 로컬 작업 폴더에서 정리(삭제)한 파일의 삭제 내역, 로컬 가상환경(`.venv-stt/`), 모델 캐시.
