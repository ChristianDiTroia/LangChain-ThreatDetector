export default function TextDisplay({
  className,
  value,
}: {
  className?: string;
  value: string;
}) {
  return (
    <div
      className={`${className} border-2 rounded-md p-2 min-h-fit bg-gray-900 shadow-xl/50`}
    >
      {value}
    </div>
  );
}
