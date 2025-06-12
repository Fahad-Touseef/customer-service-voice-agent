import React, { useState } from "react";

import { AudioPlayback } from "@/components/AudioPlayback";
import ArrowUpIcon from "@/components/icons/ArrowUpIcon";
import MicIcon from "@/components/icons/MicIcon";
import { Button } from "@/components/ui/Button";
import { cn } from "@/components/ui/utils";

interface AudioChatProps {
  startRecording: () => Promise<void>;
  stopRecording: () => Promise<Int16Array<ArrayBuffer>>;
  sendAudioMessage: (audio: Int16Array<ArrayBuffer>) => void;
  isReady: boolean;
  frequencies: number[];
}

const AudioChat = ({
  isReady = true,
  startRecording,
  stopRecording,
  sendAudioMessage,
  frequencies,
}: AudioChatProps) => {
  const [isRecording, setIsRecording] = useState(false);

  async function toggleRecording() {
    if (isRecording) {
      const audio = await stopRecording();
      sendAudioMessage(audio);
      setIsRecording(false);
    } else {
      await startRecording();
      setIsRecording(true);
    }
  }

  return (
    <Button
      variant="outline"
      size="iconSmall"
      disabled={!isReady}
      aria-label={isRecording ? "Stop Recording" : "Start Recording"}
      className={cn(
        `mb-1 me-1 [&_svg]:size-5`,
        isRecording
          ? "mr-4 bg-red-100 w-full h-full absolute top-0 left-0 z-10 flex justify-end px-4 hover:bg-red-200"
          : "mr-0 border-2 border-gray-100 hover:text-black hover:bg-gray-300 hover:border-gray-300"
      )}
      onClick={toggleRecording}
    >
      {isRecording ? (
        <div className="flex w-full justify-between items-center gap-4 h-full">
          <AudioPlayback
            playbackFrequencies={frequencies}
            itemClassName="bg-red-400 w-[4px] sm:w-[6px]"
            className="gap-[3px] w-full"
            height={36}
          />
          <Button variant="stop" size="iconSmall" asChild className="mr-2">
            <div className="!size-6 h-8 w-8 p-4">
              <ArrowUpIcon />
            </div>
          </Button>
        </div>
      ) : (
        <MicIcon />
      )}
    </Button>
  );
};

export default AudioChat;
